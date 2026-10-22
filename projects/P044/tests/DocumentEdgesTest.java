import java.util.*;
public class DocumentEdgesTest {
    public static void main(String[] args) throws Exception {
        DocumentStore s = new DocumentStore();
        s.create("D", "originale", "autore");
        List<Version> snapshot = s.history("D");
        boolean immutable = false;
        try { snapshot.clear(); } catch (UnsupportedOperationException e) { immutable = true; }
        assert immutable;
        List<Thread> workers = new ArrayList<>();
        for (int i=0;i<100;i++) workers.add(new Thread(() -> s.update("D", "nuovo", "autore")));
        for (Thread t:workers) t.start();
        for (Thread t:workers) t.join();
        assert s.latest("D").number()==101;
        assert snapshot.size()==1 && snapshot.get(0).content().equals("originale");
        for (int i=0;i<101;i++) assert s.history("D").get(i).number()==i+1;
        boolean missing=false;
        try { s.history("X"); } catch(IllegalArgumentException e) { missing=true; }
        assert missing;
        boolean invalid=false;
        try { s.create(" ","x","a"); } catch(IllegalArgumentException e) { invalid=true; }
        assert invalid;
        System.out.println("P044 PASS: snapshot immutabile e 100 aggiornamenti concorrenti");
    }
}

import java.io.*;
import java.net.*;

public class ChatIntegrationTest {
    public static void main(String[] args) throws Exception {
        try (ChatServer server = new ChatServer(0)) {
            server.start();
            try (Socket a = new Socket("127.0.0.1", server.port());
                 Socket b = new Socket("127.0.0.1", server.port())) {
                a.setSoTimeout(2000); b.setSoTimeout(2000);
                PrintWriter outA = new PrintWriter(a.getOutputStream(), true);
                PrintWriter outB = new PrintWriter(b.getOutputStream(), true);
                BufferedReader inA = new BufferedReader(new InputStreamReader(a.getInputStream()));
                BufferedReader inB = new BufferedReader(new InputStreamReader(b.getInputStream()));
                outA.println("ready-A");
                assert "ready-A".equals(inA.readLine());
                // B may receive ready-A if it is already registered.
                outB.println("ready-B");
                assert "ready-B".equals(inA.readLine());
                String ready;
                do { ready = inB.readLine(); } while ("ready-A".equals(ready));
                assert "ready-B".equals(ready);
                outA.println("ciao");
                String r1 = inA.readLine();
                String r2 = inB.readLine();
                assert "ciao".equals(r1);
                assert "ciao".equals(r2);
                System.out.println("P015: broadcast TCP PASS");
            }
        }
    }
}

import java.io.*;
import java.net.*;
import java.nio.charset.StandardCharsets;

public class ChatShutdownTest {
    public static void main(String[] args) throws Exception {
        try (ChatServer server = new ChatServer(0);
             Socket client = new Socket("127.0.0.1", server.port())) {
            server.start();
            client.setSoTimeout(1500);
            PrintWriter out = new PrintWriter(client.getOutputStream(), true, StandardCharsets.UTF_8);
            BufferedReader in = new BufferedReader(new InputStreamReader(client.getInputStream(), StandardCharsets.UTF_8));
            out.println("città e caffè");
            assert "città e caffè".equals(in.readLine());
            server.close();
            assert in.readLine() == null : "Il server deve chiudere anche i client attivi";
            server.close();
        }
        System.out.println("P015: UTF-8, chiusura con client attivo e doppia close PASS");
    }
}

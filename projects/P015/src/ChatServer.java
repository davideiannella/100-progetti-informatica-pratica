import java.io.*;
import java.net.*;
import java.nio.charset.StandardCharsets;
import java.util.*;
import java.util.concurrent.*;

public class ChatServer implements AutoCloseable {
    private final ServerSocket server;
    private final ExecutorService pool = Executors.newCachedThreadPool();
    private final Set<PrintWriter> clients = ConcurrentHashMap.newKeySet();
    private final Set<Socket> sockets = ConcurrentHashMap.newKeySet();
    private volatile boolean running = true;
    private boolean started;

    public ChatServer(int port) throws IOException { server = new ServerSocket(port, 50, InetAddress.getLoopbackAddress()); }
    public int port() { return server.getLocalPort(); }

    public synchronized void start() {
        if (!running) throw new IllegalStateException("Server chiuso");
        if (started) return;
        started = true;
        pool.submit(() -> {
            while (running) {
                try {
                    Socket socket = server.accept();
                    synchronized (this) {
                        if (!running) { socket.close(); break; }
                        sockets.add(socket);
                        pool.submit(() -> handle(socket));
                    }
                } catch (IOException e) {
                    if (running) throw new UncheckedIOException(e);
                }
            }
        });
    }
    private void handle(Socket socket) {
        PrintWriter writer = null;
        try (socket;
             BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream(), StandardCharsets.UTF_8));
             PrintWriter out = new PrintWriter(new OutputStreamWriter(socket.getOutputStream(), StandardCharsets.UTF_8), true)) {
            writer = out;
            clients.add(out);
            String line;
            while ((line = in.readLine()) != null) {
                for (PrintWriter c : clients) c.println(line);
            }
        } catch (IOException ignored) {
        } finally {
            if (writer != null) clients.remove(writer);
            sockets.remove(socket);
        }
    }
    public synchronized void close() throws IOException {
        if (!running) return;
        running = false;
        IOException failure = null;
        try { server.close(); } catch (IOException e) { failure = e; }
        for (Socket socket : sockets) {
            try { socket.close(); } catch (IOException e) { if (failure == null) failure = e; }
        }
        pool.shutdownNow();
        if (failure != null) throw failure;
    }
}

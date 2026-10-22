import java.util.*;
import java.util.concurrent.*;
import java.util.concurrent.atomic.*;
public class TicketingConcurrentTest {
    public static void main(String[] args) throws Exception {
        TicketService service = new TicketService();
        service.add(new Event("E", "Evento", 1));
        AtomicInteger success = new AtomicInteger();
        CountDownLatch ready = new CountDownLatch(12);
        CountDownLatch go = new CountDownLatch(1);
        ExecutorService pool = Executors.newFixedThreadPool(12);
        List<Future<?>> results = new ArrayList<>();
        try {
            for (int i=0; i<100; i++) {
                String user = "U" + i;
                results.add(pool.submit(() -> {
                    ready.countDown();
                    try { go.await(); service.book("E", user); success.incrementAndGet(); }
                    catch (IllegalStateException expected) { }
                    catch (InterruptedException e) { Thread.currentThread().interrupt(); throw new RuntimeException(e); }
                }));
            }
            assert ready.await(2, TimeUnit.SECONDS);
            go.countDown();
            for (Future<?> result : results) result.get(5, TimeUnit.SECONDS);
            assert success.get() == 1 && service.booked("E") == 1;
            boolean invalid = false;
            try { service.booked("NO"); } catch (IllegalArgumentException e) { invalid = true; }
            assert invalid;
        } finally { go.countDown(); pool.shutdownNow(); }
        System.out.println("P038: 100 richieste concorrenti sull’ultimo posto PASS");
    }
}

import java.util.*;
import java.util.concurrent.*;
import java.util.concurrent.atomic.*;

public class SeatBookingTest {
    public static void main(String[] args) throws Exception {
        SeatBookingService s = new SeatBookingService(3);
        ExecutorService pool = Executors.newFixedThreadPool(16);
        AtomicInteger success = new AtomicInteger();
        List<Future<?>> futures = new ArrayList<>();
        for (int i=0;i<100;i++) {
            futures.add(pool.submit(() -> { if (s.book(1)) success.incrementAndGet(); }));
        }
        for (Future<?> f : futures) f.get();
        pool.shutdown();
        assert success.get() == 1 : "Overbooking rilevato";
        assert s.book(0);
        assert !s.book(0);
        boolean bad=false;
        try { s.book(9); } catch(IllegalArgumentException e) { bad=true; }
        assert bad;
        System.out.println("P014: concorrenza PASS; prenotazioni riuscite sullo stesso posto = " + success.get());
    }
}

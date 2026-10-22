import java.util.concurrent.*;
import java.util.concurrent.locks.*;

class SeatBookingService {
    private final boolean[] booked;
    private final ReentrantLock[] locks;

    SeatBookingService(int seats) {
        if (seats <= 0) throw new IllegalArgumentException("Numero posti non valido");
        booked = new boolean[seats];
        locks = new ReentrantLock[seats];
        for (int i=0;i<seats;i++) locks[i] = new ReentrantLock();
    }

    boolean book(int seat) {
        if (seat < 0 || seat >= booked.length) throw new IllegalArgumentException("Posto fuori intervallo");
        locks[seat].lock();
        try {
            if (booked[seat]) return false;
            booked[seat] = true;
            return true;
        } finally {
            locks[seat].unlock();
        }
    }
}
public class SeatBooking {
    public static void main(String[] args) throws Exception {
        SeatBookingService s = new SeatBookingService(10);
        System.out.println(s.book(3));
    }
}

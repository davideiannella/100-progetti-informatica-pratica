import java.time.LocalDate;

public class LibraryTest {
    public static void main(String[] args) {
        LibraryService s = new LibraryService();
        s.addBook(new Book("B1","Libro"));
        s.addUser(new User("U1","Anna"));
        assert s.isAvailable("B1");
        s.lend("B1","U1", LocalDate.of(2026,10,1), 7);
        assert !s.isAvailable("B1");
        assert s.overdueCount(LocalDate.of(2026,10,9)) == 1;
        boolean duplicateLoan = false;
        try { s.lend("B1","U1", LocalDate.of(2026,10,2), 7); } catch (IllegalStateException e) { duplicateLoan = true; }
        assert duplicateLoan;
        s.returnBook("B1");
        assert s.isAvailable("B1");
        boolean missing = false;
        try { s.lend("NO","U1", LocalDate.now(), 7); } catch (IllegalArgumentException e) { missing = true; }
        assert missing;
        System.out.println("P013: 5 test PASS");
    }
}

import java.time.LocalDate;
import java.util.*;

record Book(String isbn, String title) {}
record User(String id, String name) {}
record Loan(String isbn, String userId, LocalDate startDate, LocalDate dueDate) {}

class LibraryService {
    private final Map<String, Book> books = new HashMap<>();
    private final Map<String, User> users = new HashMap<>();
    private final Map<String, Loan> activeLoans = new HashMap<>();

    void addBook(Book book) {
        if (books.putIfAbsent(book.isbn(), book) != null) throw new IllegalArgumentException("ISBN duplicato");
    }
    void addUser(User user) {
        if (users.putIfAbsent(user.id(), user) != null) throw new IllegalArgumentException("Utente duplicato");
    }
    void lend(String isbn, String userId, LocalDate start, int days) {
        if (days <= 0 || start == null) throw new IllegalArgumentException("Durata o data non valida");
        if (!books.containsKey(isbn)) throw new IllegalArgumentException("Libro inesistente");
        if (!users.containsKey(userId)) throw new IllegalArgumentException("Utente inesistente");
        if (activeLoans.containsKey(isbn)) throw new IllegalStateException("Libro già in prestito");
        activeLoans.put(isbn, new Loan(isbn, userId, start, start.plusDays(days)));
    }
    Loan returnBook(String isbn) {
        Loan loan = activeLoans.remove(isbn);
        if (loan == null) throw new IllegalStateException("Prestito inesistente");
        return loan;
    }
    boolean isAvailable(String isbn) { return books.containsKey(isbn) && !activeLoans.containsKey(isbn); }
    long overdueCount(LocalDate day) {
        return activeLoans.values().stream().filter(l -> l.dueDate().isBefore(day)).count();
    }
}

public class LibraryApp {
    public static void main(String[] args) {
        LibraryService s = new LibraryService();
        s.addBook(new Book("9780001", "Algoritmi pratici"));
        s.addUser(new User("U1", "Anna"));
        s.lend("9780001", "U1", LocalDate.of(2026, 10, 1), 14);
        System.out.println("Disponibile? " + s.isAvailable("9780001"));
    }
}

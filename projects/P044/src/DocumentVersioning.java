import java.util.*;

record Version(int number, String content, String author) {}

class DocumentStore {
    private final Map<String, List<Version>> docs = new HashMap<>();

    private void validate(String id, String content, String author) {
        if (id == null || id.isBlank() || content == null || author == null || author.isBlank())
            throw new IllegalArgumentException("invalid document");
    }
    private List<Version> versions(String id) {
        List<Version> result = docs.get(id);
        if (result == null) throw new IllegalArgumentException("missing");
        return result;
    }
    synchronized void create(String id, String content, String author) {
        validate(id, content, author);
        if (docs.containsKey(id)) throw new IllegalArgumentException("duplicate");
        docs.put(id, new ArrayList<>(List.of(new Version(1, content, author))));
    }
    synchronized Version update(String id, String content, String author) {
        validate(id, content, author);
        List<Version> list = versions(id);
        Version next = new Version(Math.addExact(list.size(), 1), content, author);
        list.add(next);
        return next;
    }
    synchronized Version latest(String id) {
        List<Version> list = versions(id);
        return list.get(list.size() - 1);
    }
    synchronized List<Version> history(String id) {
        return List.copyOf(versions(id));
    }
}
public class DocumentVersioning {
    public static void main(String[] args) {
        DocumentStore store = new DocumentStore();
        store.create("D", "v1", "anna");
        System.out.println(store.update("D", "v2", "luca"));
    }
}

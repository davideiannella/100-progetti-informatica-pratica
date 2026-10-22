static void Check(bool result) { if (!result) throw new Exception("Verifica fallita"); }
static void Expect<T>(Action action) where T : Exception {
    try { action(); } catch (T) { return; }
    throw new Exception("Eccezione attesa: " + typeof(T).Name);
}
var repo = new InMemoryReportRepository();
var create = new CreateReport(repo);
Check(repo.Get(1) == null);
Expect<ArgumentException>(() => create.Execute(0, "Guasto"));
Expect<ArgumentException>(() => create.Execute(-1, "Guasto"));
Expect<ArgumentException>(() => create.Execute(1, " "));
Expect<ArgumentException>(() => create.Execute(1, null!));
Check(repo.Get(1) == null);
var result = create.Execute(1, " Lampione spento ");
Check(result.Title == "Lampione spento" && result.Status == "OPEN");
Check(repo.Get(1) == result);
Expect<ArgumentException>(() => create.Execute(1, "Duplicato"));
Check(repo.Get(1) == result);
var fake = new FakeRepository();
new CreateReport(fake).Execute(2, "Altro guasto");
Check(fake.Last?.Id == 2 && fake.Calls == 1);
Console.WriteLine("P040: validazione, persistenza, duplicati e contratto repository PASS");
sealed class FakeRepository : IReportRepository {
    public Report? Last;
    public int Calls;
    public void Add(Report r) { Last = r; Calls++; }
    public Report? Get(int id) => Last?.Id == id ? Last : null;
}

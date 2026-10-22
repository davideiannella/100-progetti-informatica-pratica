static void Check(bool result) { if (!result) throw new Exception("Verifica fallita"); }
static void Expect<T>(Action action) where T : Exception {
    try { action(); } catch (T) { return; }
    throw new Exception("Eccezione attesa: " + typeof(T).Name);
}
var service = new MaintenanceService();
Check(service.OpenCount() == 0);
service.AddAsset(new Asset("A1", "Pompa"));
Expect<InvalidOperationException>(() => service.AddAsset(new Asset("A1", "Duplicato")));
Expect<ArgumentException>(() => service.OpenOrder("X", "NO", "Controllo"));
Expect<ArgumentException>(() => service.OpenOrder("X", "A1", "  "));
service.OpenOrder("W1", "A1", "Controllo");
Check(service.OpenCount() == 1);
Expect<InvalidOperationException>(() => service.OpenOrder("W1", "A1", "Duplicato"));
Check(service.OpenCount() == 1);
Expect<ArgumentException>(() => service.CloseOrder("NO"));
service.CloseOrder("W1");
Check(service.OpenCount() == 0);
service.CloseOrder("W1");
Check(service.OpenCount() == 0);
service.OpenOrder("W2", "A1", "Altro controllo");
Check(service.OpenCount() == 1);
Console.WriteLine("P022: manutenzioni, duplicati, input invalidi e conteggi PASS");

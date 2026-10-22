using System;
using System.Linq;
using System.Threading.Tasks;
class Program
{
    static void Check(bool condition) { if (!condition) throw new Exception("Test fallito"); }
    static void Main()
    {
        var service = new PaymentService();
        var first = service.Create("A", 1200);
        Check(Object.ReferenceEquals(first, service.Create("A", 1200)));
        Check(first.Id != service.Create("B", 1200).Id);
        bool conflict = false;
        try { service.Create("A", 1300); } catch (InvalidOperationException) { conflict = true; }
        Check(conflict);
        foreach (var key in new[] { "", " " }) {
            bool bad = false;
            try { service.Create(key, 1); } catch (ArgumentException) { bad = true; }
            Check(bad);
        }
        bool badAmount = false;
        try { service.Create("C", 0); } catch (ArgumentException) { badAmount = true; }
        Check(badAmount);
        var results = new PaymentResult[100];
        Parallel.For(0, 100, i => results[i] = service.Create("concurrent", 99));
        Check(results.All(x => Object.ReferenceEquals(x, results[0])));
        Console.WriteLine("P042 PASS: retry, conflitto, input e 100 chiamate concorrenti");
    }
}

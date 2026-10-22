using System;
using System.Collections.Generic;

public record PaymentResult(string Id, int AmountCents, string Status);

public sealed class PaymentService
{
    private readonly object gate = new();
    private readonly Dictionary<string, PaymentResult> byKey = new();

    public PaymentResult Create(string key, int amount)
    {
        if (string.IsNullOrWhiteSpace(key) || amount <= 0)
            throw new ArgumentException("Chiave e importo non validi");
        lock (gate)
        {
            if (byKey.TryGetValue(key, out var old))
            {
                if (old.AmountCents != amount)
                    throw new InvalidOperationException("Chiave riusata con importo diverso");
                return old;
            }
            var result = new PaymentResult(Guid.NewGuid().ToString("N"), amount, "ACCEPTED");
            byKey.Add(key, result);
            return result;
        }
    }
}

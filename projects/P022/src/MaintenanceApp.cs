using System;
using System.Collections.Generic;
using System.Linq;

public record Asset(string Id, string Name);
public record WorkOrder(string Id, string AssetId, string Description, bool Closed);

public sealed class MaintenanceService
{
    private readonly Dictionary<string, Asset> _assets = new();
    private readonly Dictionary<string, WorkOrder> _orders = new();

    public void AddAsset(Asset asset)
    {
        if (!_assets.TryAdd(asset.Id, asset))
            throw new InvalidOperationException("Asset duplicato");
    }

    public void OpenOrder(string id, string assetId, string description)
    {
        if (!_assets.ContainsKey(assetId))
            throw new ArgumentException("Asset inesistente");
        if (string.IsNullOrWhiteSpace(description)) throw new ArgumentException("Descrizione vuota");
        if (!_orders.TryAdd(id, new WorkOrder(id, assetId, description, false)))
            throw new InvalidOperationException("Ordine duplicato");
    }

    public void CloseOrder(string id)
    {
        if (!_orders.TryGetValue(id, out var order))
            throw new ArgumentException("Ordine inesistente");
        _orders[id] = order with { Closed = true };
    }

    public int OpenCount() => _orders.Values.Count(x => !x.Closed);
}

public static class Program
{
    public static void Main()
    {
        var service = new MaintenanceService();
        service.AddAsset(new Asset("A1", "Pompa"));
        service.OpenOrder("W1", "A1", "Controllo vibrazioni");
        Console.WriteLine(service.OpenCount());
    }
}

using Microsoft.AspNetCore.Builder;
using Microsoft.AspNetCore.Http;
using Microsoft.Extensions.DependencyInjection;
using System.Collections.Concurrent;

var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

var tasks = new ConcurrentDictionary<int, TodoItem>();
int nextId = 0;

app.MapGet("/health", () => Results.Ok(new { status = "ok" }));

app.MapGet("/tasks", () => Results.Ok(tasks.Values.OrderBy(x => x.Id)));

app.MapPost("/tasks", (CreateTodo input) =>
{
    if (string.IsNullOrWhiteSpace(input.Title))
        return Results.BadRequest(new { error = "title required" });
    var id = Interlocked.Increment(ref nextId);
    var item = new TodoItem(id, input.Title.Trim(), false);
    tasks[id] = item;
    return Results.Created($"/tasks/{id}", item);
});

app.MapPut("/tasks/{id:int}/complete", (int id) =>
{
    if (!tasks.TryGetValue(id, out var item))
        return Results.NotFound();
    var updated = item with { Completed = true };
    if (!tasks.TryUpdate(id, updated, item))
        return Results.Conflict(new { error = "retry required" });
    return Results.Ok(updated);
});

app.Run();

public record CreateTodo(string Title);
public record TodoItem(int Id, string Title, bool Completed);

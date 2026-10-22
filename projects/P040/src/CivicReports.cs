using System; using System.Collections.Generic;
public record Report(int Id,string Title,string Status);
public interface IReportRepository{void Add(Report r);Report? Get(int id);}
public sealed class CreateReport{private readonly IReportRepository repo;public CreateReport(IReportRepository r)=>repo=r;public Report Execute(int id,string title){if(id<=0 || string.IsNullOrWhiteSpace(title))throw new ArgumentException();var x=new Report(id,title.Trim(),"OPEN");repo.Add(x);return x;}}
public sealed class InMemoryReportRepository:IReportRepository{private readonly Dictionary<int,Report> m=new();public void Add(Report r)=>m.Add(r.Id,r);public Report? Get(int id)=>m.GetValueOrDefault(id);}

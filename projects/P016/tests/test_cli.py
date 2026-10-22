from pathlib import Path
import subprocess, tempfile
r=Path(__file__).resolve().parents[1]
with tempfile.TemporaryDirectory(prefix='p016_cli_') as directory:
    binary=Path(directory)/'monitor'
    subprocess.run(['gcc','-std=c11','-Wall','-Wextra','-Werror',str(r/'src/process_monitor.c'),'-o',str(binary)],check=True)
    valid=subprocess.run([str(binary)],capture_output=True,text=True,timeout=5)
    assert valid.returncode==0 and 'Name=' in valid.stdout
    for value in ['','0','-1','1x','2147483648','9999999999999999999999999999999999']:
        bad=subprocess.run([str(binary),value],capture_output=True,text=True,timeout=5)
        assert bad.returncode==2 and 'PID non valido' in bad.stderr
    assert subprocess.run([str(binary),'1','2'],capture_output=True,timeout=5).returncode==2
print('P016: esecuzione CLI, PID invalidi e overflow parsing PASS')

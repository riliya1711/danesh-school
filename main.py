import subprocess
import time

process = subprocess.Popen(['python', 'lunch.py'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

# تابعی برای خواندن خروجی خط به خط
def read_output(process):
    while True:
        output = process.stdout.readline()
        if output == '' and process.poll() is not None:
            break
        if output:
            print(output.strip())

# اجرای تابع در یک ترد جداگانه
import threading
output_thread = threading.Thread(target=read_output, args=(process,))
output_thread.start()

time.sleep(5)
process.stdin.write('1\n')
process.stdin.flush()

output_thread.join()

# بررسی خطاها
error = process.stderr.read()
if error:
    print("Error:")
    print(error.strip())

try:
    with open('lunch.py', 'r') as file:
        content = file.read()
        print("\nContent of lunch.py:")
        print(content)
except FileNotFoundError:
    print("The file lunch.py does not exist.")

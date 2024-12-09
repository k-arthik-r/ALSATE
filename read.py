import subprocess

def track_live_logs():
    log_file_path = 'live_logs.txt'
    try:
        process = subprocess.Popen(
            ['journalctl', '-f', '-o', 'short'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        while True:
            output = process.stdout.readline()
            if output: 
                with open(log_file_path, 'a') as log_file: 
                    log_file.write(output)
            elif process.poll() is not None:
                break

    except KeyboardInterrupt:
        print("\nStopping log tracking.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        process.terminate() 
    
    print(f"Logs have been saved to {log_file_path}")

if __name__ == "__main__":
    track_live_logs()

from pathlib import Path

def total_salary(path) -> float:
    
    fh = open(path, 'r')
    sum = 0
    while True:        
        lines = fh.readline()
        lines_new = lines.split(",")
        if not lines:
            break
        sum += float(lines_new[-1])
    fh.close()
    return print(sum)


way = r"D:\Python-core\HW6auto\text.txt"
path = Path(way)

if __name__ == "__main__":
    total_salary(path)
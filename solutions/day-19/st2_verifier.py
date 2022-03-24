from json import load

input_type = "data"
data = load(open(f'data/scan_rel_orient_{input_type}.json'))

detected = set()

for i in data:
    scanners, _ = i
    main, sec = scanners
    detected.add(main)
    detected.add(sec)

for i in range(5 if input_type == "sample" else 30):
    if i not in detected:
        print(i)
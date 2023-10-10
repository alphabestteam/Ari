import csv

def switch(input_file, output_file):

    input_dict = {

                "70:5a:0f:46:30:50": "Eth0", 
                "dc:4a:3e:7e:8f:2b": "Eth1",
                "70:5a:0f:44:3d:77": "Eth2", 
                "dc:4a:3e:7e:90:12": "Eth3", 
                "9c:7b:ef:aa:2c:6b": "Eth4",
                "9c:7b:ef:aa:2b:b7": "Eth5", 
                "ec:b1:d7:5b:a1:b4": "Eth6", 
                "70:5a:0d:4a:cd:c7": "Eth7"
            }
    
    with open("input_part1.csv", 'r') as input_file:
        reader = csv.reader(input_file)

        with open("output.csv", 'w', newline='') as output_file:
            writer = csv.writer(output_file)

            for row in reader:
                if row[2] in input_dict:
                    the_input = [input_dict[row[2]], row[1], row[2]]
                    writer.writerow(the_input)

                elif row[2] == "ff:ff:ff:ff:ff:ff":
                    for mac, interface in input_dict.items():
                        if mac == row[1]:
                            continue
                        the_input = [interface, row[1], mac]
                        writer.writerow(the_input)

                else:
                    writer.writerow(row)


if __name__ == '__main__':
    switch('input.csv', 'output.csv')


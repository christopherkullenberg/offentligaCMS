from wig.wig import wig
import concurrent.futures

'''
>>>> from wig.wig import wig
>>>> w = wig(url='example.com')
>>>> w.run()
>>>> results = w.get_results()
'''

urlfile = open("listamyndigheturlar.txt")
urls = urlfile.readlines()
counter = 0


def getwig(url):
    print("Scanning: " + url)
    w = wig(url=url)
    w.run()
    result = w.get_results()
    #  print(result)
    return(str(result), url)


with concurrent.futures.ProcessPoolExecutor(max_workers=100) as executor:
    for url in zip(urls, executor.map(getwig, urls)):
        print(url)
        print("Starting to write file " + str(counter))
        with open("resultatmyndigheter/" + str(counter) + ".txt", "w") as outfile:
            outfile.write(str(url))
            counter += 1
        print("Wrote to file")

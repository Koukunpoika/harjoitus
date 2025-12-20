import wikipedia

search_results = wikipedia.search("Proxmox")
print(search_results)

summary = wikipedia.summary(search_results[0])
print(summary)
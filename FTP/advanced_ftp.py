#!/usr/bin/python3

# Import necessary modules from Twisted framework
from twisted.cred.checkers import AllowAnonymousAccess, InMemoryUsernamePasswordDatabaseDontUse  # Called like that because it should not be used in production
from twisted.cred.portal import Portal  # Handles authentication for the FTP server
from twisted.internet import reactor  # Twisted's event-driven networking engine
from twisted.protocols.ftp import FTPFactory, FTPRealm  # FTP-related classes

# Create an in-memory username-password database for authentication
checker = InMemoryUsernamePasswordDatabaseDontUse()
checker.addUser("someuser", "12345")  # Add a user with username 'user' and password '12345'
checker.addUser("kali", "kali")  # Add another user

# Create an FTP realm with root directories set for anonymous and authenticated users
ftp_realm = FTPRealm('./public', userHome='/home')

# Create an authentication portal using the FTP realm and add authentication checkers
ftp_portal = Portal(ftp_realm, [AllowAnonymousAccess(), checker])

# Create an FTP factory using the portal
ftp_factory = FTPFactory(ftp_portal)

# Listen for incoming FTP connections on port 21
reactor.listenTCP(21, ftp_factory)

# Start the Twisted event loop to handle connections
reactor.run()

#!/usr/bin/python3

# Import necessary modules from Twisted framework
from twisted.cred.checkers import AllowAnonymousAccess  # Allows anonymous FTP access (not for production use)
from twisted.cred.portal import Portal  # Handles authentication for the FTP server
from twisted.internet import reactor  # Twisted's event-driven networking engine
from twisted.protocols.ftp import FTPFactory, FTPRealm  # FTP-related classes

# Create an FTP realm with the root directory set to './public'
ftp_realm = FTPRealm('./public')

# Create an authentication portal using the FTP realm and allow anonymous access
ftp_portal = Portal(ftp_realm, [AllowAnonymousAccess()])

# Create an FTP factory using the portal
ftp_factory = FTPFactory(ftp_portal)

# Listen for incoming FTP connections on port 21
reactor.listenTCP(21, ftp_factory)

# Start the Twisted event loop to handle connections
reactor.run()

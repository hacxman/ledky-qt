from PyQt4 import QtDBus, QtGui

class ServerIfc(QtDBus.QDBusAbstractInterface):

  def __init__(self, service, path, connection, parent=None):
      super(ServerIfc, self).__init__(service, path, 'cz.base48.Basebar.C', connection, parent)

  def newProductCode(self):
    m = self.call('newProductCode', 'EAN-13:5901234123457')
    print m.errorMessage()

if __name__ == '__main__':
  import sys
  app = QtGui.QApplication(sys.argv)


  server = ServerIfc('cz.base48.Basebar', '/C',
            QtDBus.QDBusConnection.sessionBus())

  server.newProductCode()

#  sys.exit(app.exec_())

import os
from zipfile import ZipFile
import xml.etree.ElementTree as ET

class KMZSensorFileReader:
    def __init__(self, rawXML):
        self.document_root = ET.fromstring(rawXML)

    def _readLookAtInfo(self, node, d):
        for i in node:
            if i.tag.endswith('longitude'):
                d['Longitude'] = float(i.text)
            if i.tag.endswith('latitude'):
                d['Latitude'] = float(i.text)

    def _createsensordictionary(self, placemark):
        d = dict()
        for i in placemark:
            if i.tag.endswith('name'):
                d['Name'] = i.text
            elif i.tag.endswith('LookAt'):
                self._readLookAtInfo(i, d)
        return d

    def _enumeratesensors(self, root):
        if root == None:
            return []
        if root.tag.find('Placemark') >= 0:
            return [self._createsensordictionary(root)]
        l = []
        for i in root:
            l.extend(self._enumeratesensors(i))
        return l

    def getsensors(self):
        """
        Returns the sensors in an enumerable collection of dictionary objects.
        """
        return self._enumeratesensors(self.document_root)

def getArterialSensors():
    THIS_DIR = os.path.dirname(os.path.realpath(__file__))
    path ='%s/../../../datasets/Phi/Sensors/ArterialSensors-I210_data_map.kmz' % THIS_DIR
    with ZipFile(path,'r') as file:
        namelist = file.namelist()
        if namelist:
            # I'm assuming the file only has one xml document.
            filereader = KMZSensorFileReader(file.read(namelist[0]).decode('utf-8'))
    return filereader.getsensors()

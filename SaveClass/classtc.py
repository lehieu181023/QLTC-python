import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Database')))
from DBconnect import DBconnect

class thucung:
    db = DBconnect()
    
    def __init__(self,matc,tuoi,loai,gt,giong,gia):
        self.matc = matc
        self.tuoi = tuoi
        self.loai = loai
        self.gt = gt
        self.giong = giong
        self.gia = gia
        
        
    def them(self):
        sql = "INSERT INTO QLTC (tuoi,loai,gt,giong,gia) VALUES ("+str(self.tuoi)+",'"+str(self.loai)+"','"+str(self.gt)+"','"+str(self.giong)+"',"+str(self.gia)+")"
        thucung.db.update(sql)
    
    def sua(self):
        sql = "UPDATE QLTC SET tuoi = "+str(self.tuoi)+", loai ='"+str(self.loai)+"',gt = '"+str(str(self.gt))+"' , giong = '"+str(self.giong)+"',gia = "+str(self.gia)+" WHERE matc = "+str(self.matc)+""
        thucung.db.update(sql)
        
    def xoa(self):
        sql = "DELETE FROM QLTC WHERE matc = "+str(self.matc)+""
        thucung.db.update(sql)
    
    def hienthi(self):
        sql = "SELECT * FROM QLTC"
        return thucung.db.hienthi(sql)
    
    def timkiemma(matc):
        sql = "SELECT * FROM QLTC WHERE matc = "+str(matc)+""
        return thucung.db.hienthi(sql)
    
    def timkiemgiong(giong):
        sql = "SELECT * FROM QLTC WHERE giong LIKE '%"+str(giong)+"%';"
        return thucung.db.hienthi(sql)
    
    


        

    
    

    
    
    
    
    
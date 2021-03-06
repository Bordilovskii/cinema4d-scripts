import c4d

def main():
    prefix = "Obj"
    separator = "_"
    doc.StartUndo()
    n = 1    
    s = doc.GetSelection()    
    for x in s: 
        doc.AddUndo(c4d.UNDOTYPE_CHANGE, x)
        x.SetName(prefix+separator+str(n))
        n = n+1
        
    c4d.EventAdd()
    doc.EndUndo()
    
if __name__=='__main__':
main()
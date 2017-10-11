package dazhong;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.UnsupportedEncodingException;

public class FileUtil {
	private File file;
	private FileOutputStream out; //如果追加方式用true        
    public FileUtil(String pathString){
    	String path=pathString;
    	file=new File(path);
    	try {
			out=new FileOutputStream(file,false);
			
			
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
    	
    }
    public void append(String str){
    	 StringBuffer sb=new StringBuffer();
    	 sb.append(str+"\n");
    	 try {
			out.write(sb.toString().getBytes("utf-8"));
		} catch (UnsupportedEncodingException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
    	 
    }
    @Override
    protected void finalize() throws Throwable {
    	// TODO Auto-generated method stub
    	super.finalize();
    	out.close();
    }
}

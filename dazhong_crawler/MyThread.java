package dazhong;

public class MyThread extends Thread {

private long start;
private long end;
private String base_url;
private PaChongUtil paChongUtil;
public MyThread(String p_base_url,long start,long end) {
	// TODO Auto-generated constructor stub
	this.start=start;
	this.end=end;
	this.base_url=p_base_url;
}
/*这个函数会在线程start的时候运行*/
@Override
public void run() {
	// TODO Auto-generated method stub
	paChongUtil = new PaChongUtil(this.base_url,"");
	/*paChongUtil是自己写的类。里面封装了一些爬取这个网站信息的一些操作
	 一个for循环遍历所有的页数，每一次就是爬取一页
	 */
	for(long i=start;i<end;i++){
		/*
		try {
			Thread.sleep(3000);
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		*/
		paChongUtil.setAppend_url(i+"");
		paChongUtil.doSearch();
	}
}
}

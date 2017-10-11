package dazhong;

import java.util.ArrayList;
import java.util.Calendar;
public class Main {
	/*这里的两个参数size对应单个线程需要负责爬取 http://www.dianping.com/rizhao/hotel 上的页数
	  threadNum是线程数
	  发现其实都是50页  我一般使用5个线程+每个线程10页
	 */
	private static long size=10;
	private static long threadNum=5;
	/*这里是一个list，用来管理所有的线程*/
	private static ArrayList<MyThread> threadList=new ArrayList<MyThread>();
	public static void main(String[] args) {
		long start_time=Calendar.getInstance().getTimeInMillis();
		
		// TODO Auto-generated method stub
		/*通过观察发现所有的页面的url格式都是 http://www.dianping.com/rizhao/hotel/p2  p后面跟着的是页码
		 所以每次只需要改变p后面的数字就好了
		 */
		String p_base_url="http://www.dianping.com/rizhao/hotel/p";
		for(int i=0;i<threadNum;i++){
			/*这个MyThread是我自己写的类，具体介绍在那个里面写*/
			MyThread myThread=new MyThread(p_base_url, 1+i*size, 1+(i+1)*size);
			threadList.add(myThread);
			/*线程start的时候会调用里面被override的run方法*/
			myThread.start();
		}
		/*这里是等待所有的线程都结束以后  输出一个over和用时*/
		try {
			for(int i=0;i<threadList.size();i++){
				threadList.get(i).join();
			}
		} catch (Exception e) {
			// TODO: handle exception
		}
		long end_time=Calendar.getInstance().getTimeInMillis();
		System.out.println(end_time-start_time+"ms");
		System.out.println("over");
	}
}

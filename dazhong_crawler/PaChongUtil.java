package dazhong;

import java.io.IOException;
import java.io.UnsupportedEncodingException;
import java.util.ArrayList;
import java.util.Calendar;
import java.util.Date;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import org.apache.http.HttpEntity;
import org.apache.http.HttpResponse;
import org.apache.http.client.ClientProtocolException;
import org.apache.http.client.HttpClient;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.impl.client.DefaultHttpClient;
import org.apache.http.util.EntityUtils;
import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;

import net.sf.json.JSONArray;
import net.sf.json.JSONObject;

public class PaChongUtil {
	private String append_url = "";
	private String base_url = "";

	public String getAppend_url() {
		return append_url;
	}

	public void setAppend_url(String append_url) {
		this.append_url = append_url;
	}

	public String getBase_url() {
		return base_url;
	}

	public void setBase_url(String base_url) {
		this.base_url = base_url;
	}

	private HttpClient httpClient = new DefaultHttpClient();

	public PaChongUtil(String p_base_url, String p_append_url) {
		this.append_url = p_append_url;
		this.base_url = p_base_url;
	}

	public void doSearch() {
		try {
			/*doPost()在下面，是private的一个方法，因为会多次使用，所以写成函数
			 参数是一个链接 ， 返回的是这个链接对应的内容，
			 这里返回的是 http://www.dianping.com/rizhao/hotel/p2 用浏览器打开这个界面显示的东西
			 */
			String html = this.doPost(base_url + append_url);
			/*这里用到了java 的正则表达式， 写一个正则表达式，在html中匹配出这个页面中包含的所有 宾馆的名字和与之对应的id 
			  这里id对应后来有关某个宾馆详情介绍的链接，比如http://www.dianping.com/newhotel/18000665   后面的18000665就是商铺的id
			  */
			Pattern pattern = Pattern.compile(" data-hippo=.*?\"content\":\"/shop/(.*?)\",\"title\":\"(.*?)\"}]'>");
			Matcher matcher = pattern.matcher(html);
			while (matcher.find()) {
				/*这个Hotel类相当于C里面的结构体，里面放了有关一个商铺需要获取的内容的字段。。方便等下输出*/
				Hotel hotel = new Hotel();
				String fileName = matcher.group(2);
				/*这里面斜杠换掉。因为这个filename是要输出的文件名，斜杠正好是文件路径下的那个斜杠，，用作文件名的话会有问题，
				 windows系统方向和mac上好像是反的，所以我直接换掉了*/
				fileName = fileName.replace("/", "%");
				fileName += "_" + matcher.group(1);
				System.out.println(fileName);
				/*这里是新建的文件夹目录*/
				FileUtil fileUtil = new FileUtil("/Users/youngtree/Desktop/YoungTree/dazhong/" + fileName + ".txt");
				/* 获取到在店铺的主页获取店铺有关的信息 比如这个页面http://www.dianping.com/newhotel/18000665   doGet是自己写的，*/
				String html3 = doGet("http://www.dianping.com/newhotel/" + matcher.group(1));
				// System.out.println(html3);
				/*这里还是一个正则表达式 匹配出json格式的有关宾馆的具体信息*/
				Pattern pattern2 = Pattern.compile("<script>window.__INITIAL_STATE__ = (.*?);</script>");
				Matcher matcher2 = pattern2.matcher(html3);
				if (matcher2.find()) {
					/*这里用了一个解析json用的jar包，我自己写了一个showJson的函数，将json格式的数据转化成hashmap的键值对的形式*/
					Map<String, String> maptemp = showJson(JSONObject.fromObject(matcher2.group(1)));
					Map<String, String> maptemp2 = showJson(JSONObject.fromObject(maptemp.get("basicInfo")));
					hotel.setName(maptemp2.get("fullName"));
					if (!maptemp2.get("price").equals(null)) {
						hotel.setAvgPrice(Integer.parseInt(maptemp2.get("price")));
					}
					hotel.setStarsLevel(maptemp2.get("shopPower"));
					hotel.setAddress(maptemp2.get("fullAdress"));
				}
				String str = base_url + append_url + "\t\t\t" + matcher.group(1) + "\t\t\t" + matcher.group(2);
				/*这就是获取评论信息的那个连接了，关于这个链接是如何找到的，要看我写的另一个文档，需要用chrome浏览器的开发者工具，
				 反正返回的是json格式的评论信息*/
				String html2 = doPost("http://www.dianping.com/hotel/pc/hotelReview?shopId=" + matcher.group(1));
				/*同样的下面开始解析*/
				JSONObject mainJson = JSONObject.fromObject(html2);
				String data = mainJson.getString("data");
				JSONObject dataJson = JSONObject.fromObject(data);
				Map<String, String> map = showJson(dataJson);
				/*将解析获取到的这些东西全部放到hotel里面*/
				hotel.setReviewCount(Integer.parseInt(map.get("reviewCountForMore")));
				hotel.setReviewCountStar1(Integer.parseInt(map.get("reviewCountStar1")));
				hotel.setReviewCountStar2(Integer.parseInt(map.get("reviewCountStar2")));
				hotel.setReviewCountStar3(Integer.parseInt(map.get("reviewCountStar3")));
				hotel.setReviewCountStar4(Integer.parseInt(map.get("reviewCountStar4")));
				hotel.setReviewCountStar5(Integer.parseInt(map.get("reviewCountStar5")));
				/*下面这些是用来得到一系列的评论并且将这些评论放到一个list里面，再将这个list放到hotel里面*/
				JSONArray jsonArray = JSONArray.fromObject(dataJson.get("reviewDataList"));
				for (int i = 0; i < jsonArray.size(); i++) {
					Map<String, String> map2 = showJson(jsonArray.getJSONObject(i));
					Map<String, String> map3 = showJson(JSONObject.fromObject(map2.get("reviewData")));
					Map<String, String> map4 = showJson(JSONObject.fromObject(map3.get("star")));
					Review review = new Review();
					review.setStarValue(map4.get("value"));
					review.setReviewBody(map3.get("reviewBody"));
					review.setTimeString(map3.get("addTime"));
					hotel.getCommentsList().add(review);
				}
				/*这个fileUtil是我自己写的用来保存文件的工具，我还写了一个hotel的getString方法，将hotel里面的信息按照一定的格式输出
				 control+鼠标左键点这个函数可以点进去看
				 */
				fileUtil.append(getString(hotel));
			}
		} catch (Exception e) {
			// TODO: handle exception
		}
	}

	private String getString(Hotel hotel) {
		StringBuffer sBuffer = new StringBuffer();
		sBuffer.append("宾馆名称 : " + hotel.getName() + "\n");
		sBuffer.append("宾馆地址 : " + hotel.getAddress() + "\n");
		sBuffer.append("宾馆均价 : " + hotel.getAvgPrice() + "\n");
		sBuffer.append("总评价数量 : " + hotel.getReviewCount() + "\n");
		sBuffer.append("一星评价 : " + hotel.getReviewCountStar1() + "\n");
		sBuffer.append("二星评价 : " + hotel.getReviewCountStar2() + "\n");
		sBuffer.append("三星评价 : " + hotel.getReviewCountStar3() + "\n");
		sBuffer.append("️四星评价 : " + hotel.getReviewCountStar4() + "\n");
		sBuffer.append("五星评价 : " + hotel.getReviewCountStar5() + "\n");
		sBuffer.append("StarsLevel : " + hotel.getStarsLevel() + "\n");
		for (int i = 0; i < hotel.getCommentsList().size(); i++) {
			sBuffer.append("----------------------------------------------------------------\n");
			sBuffer.append("评价内容 : " + hotel.getCommentsList().get(i).getReviewBody() + "\n");
			sBuffer.append("评价星数 : " + hotel.getCommentsList().get(i).getStarValue() + "\n");
			sBuffer.append("评价时间 : " + hotel.getCommentsList().get(i).getTimeString() + "\n");
		}
		return sBuffer.toString();
	}

	private Map<String, String> showJson(JSONObject jsonObject) {
		Map<String, String> map = new HashMap();
		Iterator iterator = jsonObject.keys();
		while (iterator.hasNext()) {
			String value = (String) iterator.next();
			map.put(value, jsonObject.getString(value));
		}
		return map;
	}

	private String doPost(String url) {
		String html = "";
		HttpPost httpPost = new HttpPost(url);
		httpPost.getParams().setParameter("Accept-Language", "zh-CN,zh;q=0.8,en;q=0.6");
		httpPost.getParams().setParameter("Accept-Encoding", "gzip, deflate, sdch");
		httpPost.getParams().setParameter("Content-Type", "text/html;charset=UTF-8");
		httpPost.getParams().setParameter("User-Agent",
				"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36");
		httpPost.getParams().setParameter("Accept",
				"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8");
		httpPost.getParams().setParameter("Host", "www.dianping.com");
		httpPost.getParams().setParameter("Referer", "http://www.dianping.com/rizhao/hotel");
		try {
			HttpResponse httpResponse = httpClient.execute(httpPost);
			HttpEntity entity = httpResponse.getEntity();
			html = EntityUtils.toString(entity);
		} catch (ClientProtocolException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} finally {
		}
		return html;
	}

	private String doGet(String url) {
		String html = "";
		HttpGet httpGet = new HttpGet(url);
		try {
			HttpResponse httpResponse = httpClient.execute(httpGet);
			HttpEntity entity = httpResponse.getEntity();
			html = EntityUtils.toString(entity);
		} catch (ClientProtocolException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} finally {
		}

		try {
			return new String(html.getBytes("iso8859-1"), "utf-8");
		} catch (UnsupportedEncodingException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		return "";
	}

}

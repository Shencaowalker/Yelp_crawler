package dazhong;

import java.util.ArrayList;

public class Hotel {
	private String  name ;
	private String  address ;
	private String  starsLevel ;
	private ArrayList<Review > commentsList=new ArrayList<Review >();
	private int reviewCount;
	private int reviewCountStar1;
	private int reviewCountStar2;
	private int reviewCountStar3;
	private int reviewCountStar4;
	private int reviewCountStar5;
	private int avgPrice;
	public int getAvgPrice() {
		return avgPrice;
	}
	public void setAvgPrice(int avgPrice) {
		this.avgPrice = avgPrice;
	}
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public String getAddress() {
		return address;
	}
	public void setAddress(String address) {
		this.address = address;
	}
	public String getStarsLevel() {
		return starsLevel;
	}
	public void setStarsLevel(String starsLevel) {
		this.starsLevel = starsLevel;
	}
	public ArrayList<Review> getCommentsList() {
		return commentsList;
	}
	public void setCommentsList(ArrayList<Review> commentsList) {
		this.commentsList = commentsList;
	}
	public int getReviewCount() {
		return reviewCount;
	}
	public void setReviewCount(int reviewCount) {
		this.reviewCount = reviewCount;
	}
	public int getReviewCountStar1() {
		return reviewCountStar1;
	}
	public void setReviewCountStar1(int reviewCountStar1) {
		this.reviewCountStar1 = reviewCountStar1;
	}
	public int getReviewCountStar2() {
		return reviewCountStar2;
	}
	public void setReviewCountStar2(int reviewCountStar2) {
		this.reviewCountStar2 = reviewCountStar2;
	}
	public int getReviewCountStar3() {
		return reviewCountStar3;
	}
	public void setReviewCountStar3(int reviewCountStar3) {
		this.reviewCountStar3 = reviewCountStar3;
	}
	public int getReviewCountStar4() {
		return reviewCountStar4;
	}
	public void setReviewCountStar4(int reviewCountStar4) {
		this.reviewCountStar4 = reviewCountStar4;
	}
	public int getReviewCountStar5() {
		return reviewCountStar5;
	}
	public void setReviewCountStar5(int reviewCountStar5) {
		this.reviewCountStar5 = reviewCountStar5;
	}
	
}

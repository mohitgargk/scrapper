package arbitrage;

public class FutureArbitrage implements Comparable<FutureArbitrage>{

    private long timestamp;
    private String trade;

    public FutureArbitrage() {}

    public FutureArbitrage(String trade) {
        this.trade = trade;
    }

    public String getTrade() {
        return trade;
    }

    public void setTrade(String trade) {
        this.trade = trade;
    }

    public long getTimestamp() {
        return timestamp;
    }

    public void setTimestamp(long timestamp) {
        this.timestamp = timestamp;
    }

    @Override
    public int compareTo(FutureArbitrage o) {
        if(this.getTimestamp()<o.getTimestamp())
            return 1;
        else return -1;

    }
}

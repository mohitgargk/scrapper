package arbitrage;


import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
import lombok.Data;

@JsonIgnoreProperties(ignoreUnknown = true)
@Data
public class LongStraddleTrade {

    String scrip;
    float price;
    float strike;
    float ce;
    float pe;
    float spread;
    String date;

    float maxpain_total;
    float max_p_OI_Change;
    float max_c_OI_Change;
    float maxpain_at;

    public String toString() {
        return "[" + scrip + " | " + price + " | " + strike + " | " + ce + " | " + pe + " | " +spread + " | " + date+  "]";
    }
}

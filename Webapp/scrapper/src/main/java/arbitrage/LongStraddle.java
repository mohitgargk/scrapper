package arbitrage;


import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
import lombok.Data;

@JsonIgnoreProperties(ignoreUnknown = true)
@Data
public class LongStraddle {

    String SCRIP;
    float PRICE;
    float STRIKE;
    float CE;
    float PE;
    float SPREAD;
    String date;

    float maxpain_total;
    float max_p_OI_Change;
    float max_c_OI_Change;
    float maxpain_at;

    float p1;
    float p2;
    float p3;
    float p4;
    float p5;
    float p6;
    float p7;
    float p8;
    float p9;
    float p10;
    int day;

    float breakeven;



}

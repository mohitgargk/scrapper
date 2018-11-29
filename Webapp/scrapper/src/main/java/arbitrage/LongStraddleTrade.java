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

}

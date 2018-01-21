package org.scrapper.scrapper;

import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.atomic.AtomicLong;

import arbitrage.FutureArbitrage;
import org.springframework.web.bind.annotation.*;

@RestController
public class ArbitrageController {

    private List<FutureArbitrage> arbitrages = new ArrayList<>();

    @RequestMapping(value="/arbitrage",  method = RequestMethod.GET)
    public List<FutureArbitrage> arbitrages() {
        FutureArbitrage faa = new FutureArbitrage("Infy, 2222");
        arbitrages.add(faa);
        return arbitrages;
    }

    @RequestMapping(value="/arbitrage",  method = RequestMethod.POST)
    public String arbitrageSubmit(@RequestBody FutureArbitrage fa) {
        arbitrages.add(fa);
        return "result";
    }


}

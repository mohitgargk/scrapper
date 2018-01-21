package org.scrapper.scrapper;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.stream.Collectors;

import arbitrage.FutureArbitrage;
import org.springframework.web.bind.annotation.*;

import static java.lang.Math.min;

@RestController
public class ArbitrageController {

    private List<FutureArbitrage> arbitrages = new ArrayList<>();

    @RequestMapping(value="/arbitrage",  method = RequestMethod.GET)
    public List<FutureArbitrage> arbitrages() {

        arbitrages = arbitrages.subList(0, min(arbitrages.size(), 200));
        Collections.sort(arbitrages);
        return arbitrages;
    }

    @RequestMapping(value="/arbitrage",  method = RequestMethod.POST)
    public String arbitrageSubmit(@RequestBody FutureArbitrage fa) {
        arbitrages.add(fa);
        return "result";
    }


}

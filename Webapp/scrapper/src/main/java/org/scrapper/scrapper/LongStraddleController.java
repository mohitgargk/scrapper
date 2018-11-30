package org.scrapper.scrapper;

import arbitrage.LongStraddle;
import arbitrage.LongStraddleConfig;
import arbitrage.LongStraddleTrade;
import org.scrapper.scrapper.configs.Probabilities;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;
import java.util.*;
import java.util.stream.Collectors;

@RestController
public class LongStraddleController {

    int daysLeft = 1;
    List<LongStraddleConfig> longStraddleConfigs = (new Probabilities()).getConfigs();

    private Map<String, LongStraddle> longStraddles = new HashMap<>();

    @RequestMapping(value="/ls",  method = RequestMethod.GET)
    public List<LongStraddle> getTrades() {
        return new ArrayList<>(longStraddles.values());
    }

    @RequestMapping(value="/ls",  method = RequestMethod.POST)
    public String postTrades(@RequestBody LongStraddleTrade lsc) {

        System.out.println(lsc.toString());
        LongStraddle ls = new LongStraddle();
        if(longStraddles.containsKey(lsc.getScrip()))
            ls = longStraddles.get(lsc.getScrip());

        ls.setSCRIP(lsc.getScrip());
        ls.setCE(lsc.getCe());
        ls.setPE(lsc.getPe());
        ls.setPRICE(lsc.getPrice());
        ls.setSPREAD(lsc.getSpread());
        ls.setSTRIKE(lsc.getStrike());
        ls.setDate(lsc.getDate());

        longStraddles.put(lsc.getScrip(),ls);

        return "OK";
    }

    @RequestMapping(value="/n",  method = RequestMethod.POST)
    public String postN(@RequestBody Integer i) {

        daysLeft=i;
        longStraddleConfigs = (new Probabilities()).getConfigs()
                .stream()
                .filter(c -> c.getDay()==daysLeft)
                .collect(Collectors.toList());

        setConfigs(longStraddleConfigs);


        return "OK";
    }


    @RequestMapping(value="/n",  method = RequestMethod.GET)
    public Integer getN(@RequestBody Integer i) {
        return daysLeft;
    }

    @RequestMapping(value="/lsconfig",  method = RequestMethod.GET)
    public List<LongStraddleConfig> getConfigs() {
        return (new ArrayList<LongStraddle>(longStraddles.values()))
                .stream()
                .map(ls -> {
                    LongStraddleConfig lsc = new LongStraddleConfig();
                    lsc.setScrip(ls.getSCRIP());
                    lsc.setDay(ls.getDay());
                    lsc.setP1(ls.getP1());
                    lsc.setP2(ls.getP2());
                    lsc.setP3(ls.getP3());
                    lsc.setP4(ls.getP4());
                    lsc.setP5(ls.getP5());
                    lsc.setP6(ls.getP6());
                    lsc.setP7(ls.getP7());
                    lsc.setP8(ls.getP8());
                    lsc.setP9(ls.getP9());
                    lsc.setP10(ls.getP10());
                    return  lsc;
                }).collect(Collectors.toList());
    }


    @RequestMapping(value="/lsconfig",  method = RequestMethod.POST)
    public String setConfigs(@RequestBody List<LongStraddleConfig> longStraddleConfigs) {

        for(LongStraddleConfig lsc : longStraddleConfigs) {

            LongStraddle ls = new LongStraddle();
            if(longStraddles.containsKey(lsc.getScrip()))
                ls = longStraddles.get(lsc.getScrip());

            ls.setP1(lsc.getP1());
            ls.setP2(lsc.getP2());
            ls.setP3(lsc.getP3());
            ls.setP4(lsc.getP4());
            ls.setP5(lsc.getP5());
            ls.setP6(lsc.getP6());
            ls.setP7(lsc.getP7());
            ls.setP8(lsc.getP8());
            ls.setP8(lsc.getP9());
            ls.setP8(lsc.getP10());

            ls.setSCRIP(lsc.getScrip());
            longStraddles.put(lsc.getScrip(),ls);
        }

        return "OK";
    }


}

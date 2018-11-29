package org.scrapper.scrapper.configs;

import arbitrage.LongStraddleConfig;
import com.google.gson.Gson;
import lombok.Data;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

@Data
public class Probabilities {

    List<LongStraddleConfig> configs = new ArrayList<>();

    public Probabilities()  {


        ClassLoader classLoader = getClass().getClassLoader();
        File file = new File("probability.json");

        StringBuilder stringBuilder = new StringBuilder();
        try {
            BufferedReader reader = new BufferedReader(new FileReader(file));
            String line = null;
            while ((line = reader.readLine()) != null) {
                stringBuilder.append(line);
            }
            reader.close();
        }
        catch (Exception ex) {
            ex.printStackTrace();
        }
        String content = stringBuilder.toString();

        Gson gson = new Gson();
        configs = new ArrayList<>(Arrays.asList( gson.fromJson(content, LongStraddleConfig[].class)));
    }
}

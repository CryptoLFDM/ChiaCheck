# ChiaCheck

This utility is designed to run ``chia plot check`` command and compute result.

## Requierement

python3 is required. Chia node is not required, we use chia package instead.

## How to install

``pip install -r requirements.txt``

## How to run

````
Options:
  --pseudo TEXT          Pseudo to search on grafana  [required]
  --chia_root_path TEXT  chia root path  [required]
  --challenge INTEGER    The number of challenge for each plot
  --help                 Show this message and exit.

````
default challenge is 32.

``python main.py --pseudo Douceur --chia_root_path /chia``

## Result

### Console Mode

````
2023-04-28 19:18:51,327 INFO | dissect_log | going to test plot size k32 in /mnt/sdg with name plot-k32-2021-08-18-03-04-b779d30408d3983cf4ee4476f54440645bd4c1d5b20e2278f6170ecaa01bb217.plot
2023-04-28 19:18:51,327 INFO | dissect_log | plot-k32-2021-08-18-03-04-b779d30408d3983cf4ee4476f54440645bd4c1d5b20e2278f6170ecaa01bb217.plot is having xch1yl3mnukcd2f69vxuava62msp5y7qvjwuq9rc55dcfj3jw4a92t2sgp4dwh contract pool
2023-04-28 19:18:51,328 INFO | dissect_log | plot-k32-2021-08-18-03-04-b779d30408d3983cf4ee4476f54440645bd4c1d5b20e2278f6170ecaa01bb217.plot is having b162c4b81fbf8d0aae876db016e28292509d69c2ce01227304d879222cb435092105b1f414f2d263a8c920ad44851096 farmer key
2023-04-28 19:18:51,328 FAILED | dissect_log | plot-k32-2021-08-18-03-04-b779d30408d3983cf4ee4476f54440645bd4c1d5b20e2278f6170ecaa01bb217.plot is having 0.75 quality with score 24 / 32
2023-04-28 19:18:51,334 INFO | dissect_log | going to test plot size k32 in /mnt/sdg with name plot-k32-2021-08-19-04-25-fac9d51eafc23a634e8ccb04f09943fd06fa2ecb5613a0e80460432d9ebb8ea7.plot
2023-04-28 19:18:51,334 INFO | dissect_log | plot-k32-2021-08-19-04-25-fac9d51eafc23a634e8ccb04f09943fd06fa2ecb5613a0e80460432d9ebb8ea7.plot is having xch1yl3mnukcd2f69vxuava62msp5y7qvjwuq9rc55dcfj3jw4a92t2sgp4dwh contract pool
2023-04-28 19:18:51,334 INFO | dissect_log | plot-k32-2021-08-19-04-25-fac9d51eafc23a634e8ccb04f09943fd06fa2ecb5613a0e80460432d9ebb8ea7.plot is having b162c4b81fbf8d0aae876db016e28292509d69c2ce01227304d879222cb435092105b1f414f2d263a8c920ad44851096 farmer key
2023-04-28 19:18:51,334 SUCCESS | dissect_log | plot-k32-2021-08-19-04-25-fac9d51eafc23a634e8ccb04f09943fd06fa2ecb5613a0e80460432d9ebb8ea7.plot is having 0.875 quality with score 28 / 32
2023-04-28 19:18:51,335 INFO | dissect_log | going to test plot size k32 in /mnt/sdg with name plot-k32-2021-08-19-07-08-a4d06c4dd261b63bdf34ee9677fa99fe0a2fe6400d7666b46666a3397a1e440b.plot
2023-04-28 19:18:51,335 INFO | dissect_log | plot-k32-2021-08-19-07-08-a4d06c4dd261b63bdf34ee9677fa99fe0a2fe6400d7666b46666a3397a1e440b.plot is having xch1yl3mnukcd2f69vxuava62msp5y7qvjwuq9rc55dcfj3jw4a92t2sgp4dwh contract pool
2023-04-28 19:18:51,335 INFO | dissect_log | plot-k32-2021-08-19-07-08-a4d06c4dd261b63bdf34ee9677fa99fe0a2fe6400d7666b46666a3397a1e440b.plot is having b162c4b81fbf8d0aae876db016e28292509d69c2ce01227304d879222cb435092105b1f414f2d263a8c920ad44851096 farmer key
2023-04-28 19:18:51,335 SUCCESS | dissect_log | plot-k32-2021-08-19-07-08-a4d06c4dd261b63bdf34ee9677fa99fe0a2fe6400d7666b46666a3397a1e440b.plot is having 0.8125 quality with score 26 / 32
2023-04-28 19:18:51,335 INFO | dissect_log | going to test plot size k32 in /mnt/sdg with name plot-k32-2021-08-19-09-24-a92ae7b47d0a707e1d951ec914e2faf33f1b0ea012efcdc40c3c203c70c4379b.plot
2023-04-28 19:18:51,335 INFO | dissect_log | plot-k32-2021-08-19-09-24-a92ae7b47d0a707e1d951ec914e2faf33f1b0ea012efcdc40c3c203c70c4379b.plot is having xch1yl3mnukcd2f69vxuava62msp5y7qvjwuq9rc55dcfj3jw4a92t2sgp4dwh contract pool
2023-04-28 19:18:51,335 INFO | dissect_log | plot-k32-2021-08-19-09-24-a92ae7b47d0a707e1d951ec914e2faf33f1b0ea012efcdc40c3c203c70c4379b.plot is having b162c4b81fbf8d0aae876db016e28292509d69c2ce01227304d879222cb435092105b1f414f2d263a8c920ad44851096 farmer key
2023-04-28 19:18:51,336 SUCCESS | dissect_log | plot-k32-2021-08-19-09-24-a92ae7b47d0a707e1d951ec914e2faf33f1b0ea012efcdc40c3c203c70c4379b.plot is having 1.0 quality with score 32 / 32
2023-04-28 19:18:51,336 INFO | dissect_log | going to test plot size k32 in /mnt/sdg with name plot-k32-2021-08-19-09-47-dc6f6a102fe4dad20e60d3d7d805e95075479b9968d2499929b562946adbb092.plot
2023-04-28 19:18:51,336 INFO | dissect_log | plot-k32-2021-08-19-09-47-dc6f6a102fe4dad20e60d3d7d805e95075479b9968d2499929b562946adbb092.plot is having xch1yl3mnukcd2f69vxuava62msp5y7qvjwuq9rc55dcfj3jw4a92t2sgp4dwh contract pool
2023-04-28 19:18:51,336 INFO | dissect_log | plot-k32-2021-08-19-09-47-dc6f6a102fe4dad20e60d3d7d805e95075479b9968d2499929b562946adbb092.plot is having b162c4b81fbf8d0aae876db016e28292509d69c2ce01227304d879222cb435092105b1f414f2d263a8c920ad44851096 farmer key
2023-04-28 19:18:51,336 SUCCESS | dissect_log | plot-k32-2021-08-19-09-47-dc6f6a102fe4dad20e60d3d7d805e95075479b9968d2499929b562946adbb092.plot is having 0.9062 quality with score 29 / 32
2023-04-28 19:18:51,336 SUCCESS | dissect_log | 832 plots found => 82.34554 TiB
2023-04-28 19:18:51,341 HIGHLIGHT | dissect_log | See result on https://mythologic.fr/d/k9v1FlP4z/chia-plot-check-summary?orgId=7&var-Pseudo=Douceur&refresh=30s

````

### Grafana visu

[See Result on Mythologic.fr](https://mythologic.fr/d/k9v1FlP4z/chia-plot-check-summary?orgId=7&from=now-30d&to=now)
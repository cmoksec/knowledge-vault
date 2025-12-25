# Practice: DAST

Created: June 25, 2025 10:32 PM

```yaml
#Sample DAST check
zap-check:  
  stage: runDAST  
  before_script: [ ]  
  image:  
    name: ghcr.io/zaproxy/zaproxy:latest  
    entrypoint: [ "" ]  
  variables:  
    ZAP_REPORT_DIR: /zap/wrk/  
    ZAP_REPORT: report_site.html  
  script:  
    - mkdir -p ${ZAP_REPORT_DIR}  
    - zap-baseline.py -t https://example.com -r ${ZAP_REPORT} || true  
    - cp ${ZAP_REPORT_DIR}${ZAP_REPORT} ${ZAP_REPORT}  
  artifacts:  
    when: always  
    expire_in: 1 week  
    paths:  
      - ${ZAP_REPORT}  
```
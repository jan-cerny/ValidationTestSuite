Description
This test content should run on any platform and test CPE applicability.
It uses platform independent CPE's.

Content Status
Complete

Testing Status
Complete

Known Issues
None

Scripts
None

Configuration Instructions
None

Running Instructions and Expected Results
	1. Test case: Benchmark applicability
		Run the data stream by selecting the benchmark:
			a. Benchmark id="xccdf_gov.nist_benchmark_r1200-1" - expected result: Applicable
				Group id="xccdf_gov.nist_group_cpe_applicability-1"\rule id="xccdf_gov.nist_rule_r1200_cpe_applicability-1 - expected result: NOTSELECTED | (rule result n/a)
				Group id="xccdf_gov.nist_group_cpe_applicability-1"\rule id="xccdf_gov.nist_rule_r1200_cpe_applicability-2 - expected result: NOTSELECTED | (rule result n/a)
				Group id="xccdf_gov.nist_group_cpe_applicability-1"\rule id="xccdf_gov.nist_rule_r1200_cpe_applicability-3 - expected result: NOTSELECTED | (rule result n/a)
				Group id="xccdf_gov.nist_group_cpe_applicability-1"\rule id="xccdf_gov.nist_rule_r1200_cpe_applicability-4 - expected result: NOTSELECTED | (rule result n/a)
				Group id="xccdf_gov.nist_group_cpe_applicability-1"\rule id="xccdf_gov.nist_rule_r1200_cpe_applicability-5 - expected result: NOTSELECTED | (rule result n/a)
				Group id="xccdf_gov.nist_group_cpe_applicability-1"\rule id="xccdf_gov.nist_rule_r1200_cpe_applicability-6 - expected result: NOTSELECTED | (rule result n/a)
				Group id="xccdf_gov.nist_group_cpe_applicability-1"\rule id="xccdf_gov.nist_rule_r1200_cpe_applicability-7 - expected result: NOTSELECTED | (rule result n/a)
				Group id="xccdf_gov.nist_group_cpe_applicability-2"\rule id="xccdf_gov.nist_rule_r1200_cpe_applicability-8 - expected result: Not Applicable | (rule result n/a)
				(No_Group)\rule id="xccdf_gov.nist_rule_r1200_cpe_applicability-9 - expected result: NOTSELECTED | (rule result n/a)
				(No_Group)\rule id="xccdf_gov.nist_rule_r1200_cpe_applicability-10 - expected result: Not Applicable | (rule result n/a)
				(No_Group)\rule id="xccdf_gov.nist_rule_r1200_cpe_applicability-11 - expected result: NOTSELECTED | (rule result n/a)
				(No_Group)\rule id="xccdf_gov.nist_rule_r1200_cpe_applicability-12 - expected result: Not Applicable | (rule result n/a)
			
			b. Benchmark id="xccdf_gov.nist_benchmark_r1200-2" - expected result: Not Applicable
			
			c. Benchmark id="xccdf_gov.nist_benchmark_r1200-3" - expected result: Applicable
				Group id="xccdf_gov.nist_group_cpe_applicability-100"\xccdf_gov.nist_rule_r1200_cpe_applicability-100 - expected result: Applicable | (rule result PASS)
				(No_Group)\xccdf_gov.nist_rule_r1200_cpe_applicability-200 - expected result: NOTSELECTED | (rule result n/a)
			
			d. Benchmark id="xccdf_gov.nist_benchmark_r1200-4" - expected result: Applicable
				Group id="xccdf_gov.nist_group_cpe_applicability-1000"\xccdf_gov.nist_rule_r1200_cpe_applicability-1000 - expected result: Applicable | (rule result PASS)
				Group id="xccdf_gov.nist_group_cpe_applicability-1000"xccdf_gov.nist_rule_r1200_cpe_applicability-2000 - expected result: Applicable | (rule result FAIL)
				Group id="xccdf_gov.nist_group_cpe_applicability-2000"xccdf_gov.nist_rule_r1200_cpe_applicability-8000 - expected result: Not Applicable | (rule result n/a)
			
			e. Benchmark id="xccdf_gov.nist_benchmark_r1200-5" - expected result: Not Applicable
		
		or 
		
		Run the data stream by selecting the checklists\component-ref @id:
			f. Checklist id="scap_gov.nist_cref_r1200-xccdf1.xml" - expected result: Applicable
				Group id="xccdf_gov.nist_group_cpe_applicability-1"\rule id="xccdf_gov.nist_rule_r1200_cpe_applicability-1 - expected result: NOTSELECTED | (rule result n/a)
				Group id="xccdf_gov.nist_group_cpe_applicability-1"\rule id="xccdf_gov.nist_rule_r1200_cpe_applicability-2 - expected result: NOTSELECTED | (rule result n/a)
				Group id="xccdf_gov.nist_group_cpe_applicability-1"\rule id="xccdf_gov.nist_rule_r1200_cpe_applicability-3 - expected result: NOTSELECTED | (rule result n/a)
				Group id="xccdf_gov.nist_group_cpe_applicability-1"\rule id="xccdf_gov.nist_rule_r1200_cpe_applicability-4 - expected result: NOTSELECTED | (rule result n/a)
				Group id="xccdf_gov.nist_group_cpe_applicability-1"\rule id="xccdf_gov.nist_rule_r1200_cpe_applicability-5 - expected result: NOTSELECTED | (rule result n/a)
				Group id="xccdf_gov.nist_group_cpe_applicability-1"\rule id="xccdf_gov.nist_rule_r1200_cpe_applicability-6 - expected result: NOTSELECTED | (rule result n/a)
				Group id="xccdf_gov.nist_group_cpe_applicability-1"\rule id="xccdf_gov.nist_rule_r1200_cpe_applicability-7 - expected result: NOTSELECTED | (rule result n/a)
				Group id="xccdf_gov.nist_group_cpe_applicability-2"\rule id="xccdf_gov.nist_rule_r1200_cpe_applicability-8 - expected result: Not Applicable | (rule result n/a)
				(No_Group)\rule id="xccdf_gov.nist_rule_r1200_cpe_applicability-9 - expected result: NOTSELECTED | (rule result n/a)
				(No_Group)\rule id="xccdf_gov.nist_rule_r1200_cpe_applicability-10 - expected result: Not Applicable | (rule result n/a)
				(No_Group)\rule id="xccdf_gov.nist_rule_r1200_cpe_applicability-11 - expected result: NOTSELECTED | (rule result n/a)
				(No_Group)\rule id="xccdf_gov.nist_rule_r1200_cpe_applicability-12 - expected result: Not Applicable | (rule result n/a)
			
			g. Checklist id="scap_gov.nist_cref_r1200-xccdf2.xml" - expected result: Not Applicable
			
			h. Checklist id="scap_gov.nist_cref_r1200-xccdf3.xml" - expected result: Applicable
				Group id="xccdf_gov.nist_group_cpe_applicability-100"\xccdf_gov.nist_rule_r1200_cpe_applicability-100 - expected result: Applicable | (rule result PASS)
				(No_Group)\xccdf_gov.nist_rule_r1200_cpe_applicability-200 - expected result: NOTSELECTED | (rule result n/a)
			
			i. Checklist id="scap_gov.nist_cref_r1200-xccdf4.xml" - expected result: Applicable
				Group id="xccdf_gov.nist_group_cpe_applicability-1000"\xccdf_gov.nist_rule_r1200_cpe_applicability-1000 - expected result: Applicable | (rule result PASS)
				Group id="xccdf_gov.nist_group_cpe_applicability-1000"xccdf_gov.nist_rule_r1200_cpe_applicability-2000 - expected result: Applicable | (rule result FAIL)
				Group id="xccdf_gov.nist_group_cpe_applicability-2000"xccdf_gov.nist_rule_r1200_cpe_applicability-8000 - expected result: Not Applicable | (rule result n/a)
			
			j. Checklist id="scap_gov.nist_cref_r1200-xccdf5.xml" - expected result: Not Applicable			
			
	
	2. Test case: Group applicability
		Run the data stream by selecting a profile id:
			a. Profile id="xccdf_gov.nist.validation_profile_cpe_applicability_1"
				- Group id="xccdf_gov.nist_group_cpe_applicability-1" - expected result: Applicable
			b. Profile id="xccdf_gov.nist.validation_profile_cpe_applicability_1"
				- Group id="xccdf_gov.nist_group_cpe_applicability-2" - expected result: Not Applicable
			c. Profile id="xccdf_gov.nist.validation_profile_cpe_applicability_3"
				- Group id="xccdf_gov.nist_group_cpe_applicability-100" - expected result: Applicable
			d. Profile id="xccdf_gov.nist.validation_profile_cpe_applicability_4"
				- Group id="xccdf_gov.nist_group_cpe_applicability-1000" - expected result: Applicable
			e. Profile id="xccdf_gov.nist.validation_profile_cpe_applicability_4"
				- Group id="xccdf_gov.nist_group_cpe_applicability-2000" - expected result: Not Applicable


	3. Test case: Rule applicability
		Run the data stream by selecting a profile id:
			a. Profile id="xccdf_gov.nist.validation_profile_cpe_applicability_1"
				Group id="xccdf_gov.nist_group_cpe_applicability-1"\rule id="xccdf_gov.nist_rule_r1200_cpe_applicability-1 - expected result: Applicable | (rule result PASS)
				Group id="xccdf_gov.nist_group_cpe_applicability-1"\rule id="xccdf_gov.nist_rule_r1200_cpe_applicability-2 - expected result: Not Applicable | (rule result n/a)
				Group id="xccdf_gov.nist_group_cpe_applicability-1"\rule id="xccdf_gov.nist_rule_r1200_cpe_applicability-3 - expected result: Applicable | (rule result PASS)
				Group id="xccdf_gov.nist_group_cpe_applicability-1"\rule id="xccdf_gov.nist_rule_r1200_cpe_applicability-4 - expected result: Not Applicable | (rule result n/a)
				Group id="xccdf_gov.nist_group_cpe_applicability-1"\rule id="xccdf_gov.nist_rule_r1200_cpe_applicability-5 - expected result: Applicable | (rule result PASS)
				Group id="xccdf_gov.nist_group_cpe_applicability-1"\rule id="xccdf_gov.nist_rule_r1200_cpe_applicability-6 - expected result: Applicable | (rule result PASS)
				Group id="xccdf_gov.nist_group_cpe_applicability-1"\rule id="xccdf_gov.nist_rule_r1200_cpe_applicability-7 - expected result: Not Applicable | (rule result n/a)
				Group id="xccdf_gov.nist_group_cpe_applicability-2"\rule id="xccdf_gov.nist_rule_r1200_cpe_applicability-8 - expected result: Not Applicable | (rule result n/a)
				(No_Group)\rule id="xccdf_gov.nist_rule_r1200_cpe_applicability-9 - expected result: Applicable| (rule result PASS)
				(No_Group)\rule id="xccdf_gov.nist_rule_r1200_cpe_applicability-10 - expected result: Not Applicable | (rule result n/a)
				(No_Group)\rule id="xccdf_gov.nist_rule_r1200_cpe_applicability-11 - expected result: Applicable| (rule result PASS)
				(No_Group)\rule id="xccdf_gov.nist_rule_r1200_cpe_applicability-12 - expected result: Not Applicable | (rule result n/a)

			b. Profile id="xccdf_gov.nist.validation_profile_cpe_applicability_2"  - expected result: Not Applicable | (rule result n/a)
				

	SCAP Interpreter examples:
		step: 1.a - N/A
		step: 1.b - N/A
		step: 1.c - N/A
		step: 1.d - N/A
		step: 1.e - N/A
		step: 1.f
			java -jar scap-exec-1.2.5.jar -c scap_gov.nist_cref_r1200-xccdf1.xml r1200-datastream.xml -f results-r1200-datastream-1f.xml
		step: 1.g
			java -jar scap-exec-1.2.5.jar -c scap_gov.nist_cref_r1200-xccdf2.xml r1200-datastream.xml -f results-r1200-datastream-1g.xml
		step: 1.h
			java -jar scap-exec-1.2.5.jar -c scap_gov.nist_cref_r1200-xccdf3.xml r1200-datastream.xml -f results-r1200-datastream-1h.xml
		step: 1.i
			java -jar scap-exec-1.2.5.jar -c scap_gov.nist_cref_r1200-xccdf4.xml r1200-datastream.xml -f results-r1200-datastream-1i.xml
		step: 1.j
			java -jar scap-exec-1.2.5.jar -c scap_gov.nist_cref_r1200-xccdf5.xml r1200-datastream.xml -f results-r1200-datastream-1j.xml
			
		step: 2.a
			java -jar scap-exec-1.2.5.jar -c scap_gov.nist_cref_r1200-xccdf1.xml -p xccdf_gov.nist.validation_profile_cpe_applicability_1 r1200-datastream.xml -f results-r1200-datastream-2a.xml
		step: 2.b
			java -jar scap-exec-1.2.5.jar -c scap_gov.nist_cref_r1200-xccdf2.xml -p xccdf_gov.nist.validation_profile_cpe_applicability_1 r1200-datastream.xml -f results-r1200-datastream-2b.xml
		step: 2.c
			java -jar scap-exec-1.2.5.jar -c scap_gov.nist_cref_r1200-xccdf3.xml -p xccdf_gov.nist.validation_profile_cpe_applicability_3 r1200-datastream.xml -f results-r1200-datastream-2c.xml
		step: 2.d
			java -jar scap-exec-1.2.5.jar -c scap_gov.nist_cref_r1200-xccdf4.xml -p xccdf_gov.nist.validation_profile_cpe_applicability_4 r1200-datastream.xml -f results-r1200-datastream-2d.xml
		step: 2.e
			(it's the same command as 2.d, but group xccdf_gov.nist_group_cpe_applicability-2000 should not be applicable)
			java -jar scap-exec-1.2.5.jar -c scap_gov.nist_cref_r1200-xccdf4.xml -p xccdf_gov.nist.validation_profile_cpe_applicability_4 r1200-datastream.xml -f results-r1200-datastream-2e.xml
			
		step: 3.a
			java -jar scap-exec-1.2.5.jar -c scap_gov.nist_cref_r1200-xccdf1.xml -p xccdf_gov.nist.validation_profile_cpe_applicability_1 r1200-datastream.xml -f results-r1200-datastream-3a.xml
		step: 3.b
			java -jar scap-exec-1.2.5.jar -c scap_gov.nist_cref_r1200-xccdf2.xml -p xccdf_gov.nist.validation_profile_cpe_applicability_2 r1200-datastream.xml -f results-r1200-datastream-3b.xml


Cleanup Instructions 
None
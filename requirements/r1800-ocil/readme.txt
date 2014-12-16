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
			a. Benchmark id="xccdf_gov.nist_benchmark_r1800-ocil-1" - expected result: Applicable
				Group1\rule id="xccdf_gov.nist_rule_r1800-ocil_cpe_applicability-1 - expected result: NOTSELECTED | (rule result n/a)
				Group1\rule id="xccdf_gov.nist_rule_r1800-ocil_cpe_applicability-2 - expected result: NOTSELECTED | (rule result n/a)
				Group1\rule id="xccdf_gov.nist_rule_r1800-ocil_cpe_applicability-3 - expected result: NOTSELECTED | (rule result n/a)
				Group1\rule id="xccdf_gov.nist_rule_r1800-ocil_cpe_applicability-4 - expected result: NOTSELECTED | (rule result n/a)
				Group1\rule id="xccdf_gov.nist_rule_r1800-ocil_cpe_applicability-5 - expected result: NOTSELECTED | (rule result n/a)
				Group1\rule id="xccdf_gov.nist_rule_r1800-ocil_cpe_applicability-6 - expected result: NOTSELECTED | (rule result n/a)
				Group1\rule id="xccdf_gov.nist_rule_r1800-ocil_cpe_applicability-7 - expected result: NOTSELECTED | (rule result n/a)
				Group2\rule id="xccdf_gov.nist_rule_r1800-ocil_cpe_applicability-8 - expected result: Not Applicable | (rule result n/a)
				(No_Group)\rule id="xccdf_gov.nist_rule_r1800-ocil_cpe_applicability-9 - expected result: NOTSELECTED | (rule result n/a)
				(No_Group)\rule id="xccdf_gov.nist_rule_r1800-ocil_cpe_applicability-10 - expected result: Not Applicable | (rule result n/a)
			
			b. Benchmark id="xccdf_gov.nist_benchmark_r1800-ocil-2" - expected result: Not Applicable
		
		or 
		
		Run the data stream by selecting the checklists\component-ref @id:
			c. Checklist id="scap_gov.nist_cref_r1800-ocil-xccdf1.xml" - expected result: Applicable
				Group1\rule id="xccdf_gov.nist_rule_r1800-ocil_cpe_applicability-1 - expected result: NOTSELECTED | (rule result n/a)
				Group1\rule id="xccdf_gov.nist_rule_r1800-ocil_cpe_applicability-2 - expected result: NOTSELECTED | (rule result n/a)
				Group1\rule id="xccdf_gov.nist_rule_r1800-ocil_cpe_applicability-3 - expected result: NOTSELECTED | (rule result n/a)
				Group1\rule id="xccdf_gov.nist_rule_r1800-ocil_cpe_applicability-4 - expected result: NOTSELECTED | (rule result n/a)
				Group1\rule id="xccdf_gov.nist_rule_r1800-ocil_cpe_applicability-5 - expected result: NOTSELECTED | (rule result n/a)
				Group1\rule id="xccdf_gov.nist_rule_r1800-ocil_cpe_applicability-6 - expected result: NOTSELECTED | (rule result n/a)
				Group1\rule id="xccdf_gov.nist_rule_r1800-ocil_cpe_applicability-7 - expected result: NOTSELECTED | (rule result n/a)
				Group2\rule id="xccdf_gov.nist_rule_r1800-ocil_cpe_applicability-8 - expected result: Not Applicable | (rule result n/a)
				(No_Group)\rule id="xccdf_gov.nist_rule_r1800-ocil_cpe_applicability-9 - expected result: NOTSELECTED | (rule result n/a)
				(No_Group)\rule id="xccdf_gov.nist_rule_r1800-ocil_cpe_applicability-10 - expected result: Not Applicable | (rule result n/a)
			
			d. Checklist id="scap_gov.nist_cref_r1800-ocil-xccdf2.xml" - expected result: Not Applicable
	
	2. Test case: Group applicability
		Run the data stream by selecting a profile id:
			a. Profile id="xccdf_gov.nist.r1800-ocil_profile_cpe_applicability_1"
				- Group id="xccdf_gov.nist_group_ocil_cpe_applicability-1" - expected result: Applicable
			b. Profile id="xccdf_gov.nist.r1800-ocil_profile_cpe_applicability_1"
				- Group id="xccdf_gov.nist_group_ocil_cpe_applicability-2" - expected result: Not Applicable
	
	3. Test case: Rule applicability
		Run the data stream by selecting a profile id:
			a. Profile id="xccdf_gov.nist.r1800-ocil_profile_cpe_applicability_1"
				Group1\rule id="xccdf_gov.nist_rule_r1800-ocil_cpe_applicability-1 - expected result: Applicable | (rule result PASS)
				Group1\rule id="xccdf_gov.nist_rule_r1800-ocil_cpe_applicability-2 - expected result: Not Applicable | (rule result n/a)
				Group1\rule id="xccdf_gov.nist_rule_r1800-ocil_cpe_applicability-3 - expected result: Applicable | (rule result PASS)
				Group1\rule id="xccdf_gov.nist_rule_r1800-ocil_cpe_applicability-4 - expected result: Not Applicable | (rule result n/a)
				Group1\rule id="xccdf_gov.nist_rule_r1800-ocil_cpe_applicability-5 - expected result: Applicable | (rule result PASS)
				Group1\rule id="xccdf_gov.nist_rule_r1800-ocil_cpe_applicability-6 - expected result: Applicable | (rule result PASS)
				Group1\rule id="xccdf_gov.nist_rule_r1800-ocil_cpe_applicability-7 - expected result: Not Applicable | (rule result n/a)
				Group2\rule id="xccdf_gov.nist_rule_r1800-ocil_cpe_applicability-8 - expected result: Not Applicable | (rule result n/a)
				(No_Group)\rule id="xccdf_gov.nist_rule_r1800-ocil_cpe_applicability-9 - expected result: Applicable| (rule result PASS)
				(No_Group)\rule id="xccdf_gov.nist_rule_r1800-ocil_cpe_applicability-10 - expected result: Not Applicable | (rule result n/a)

			b. Profile id="xccdf_gov.nist.r1800-ocil_profile_cpe_applicability_2"  - expected result: Not Applicable | (rule result n/a)
				

	SCAP Interpreter examples:
		step: 1.a - N/A
		step: 1.b - N/A
		step: 1.c
			java -jar scap-exec-1.2.5.jar -c scap_gov.nist_cref_r1800-ocil-xccdf1.xml r1800-ocil-datastream.xml -f results-r1800-ocil-datastream-1.xml
		step: 1.d
			java -jar scap-exec-1.2.5.jar -c scap_gov.nist_cref_r1800-ocil-xccdf2.xml r1800-ocil-datastream.xml -f results-r1800-ocil-datastream-2.xml
			
		step: 2.a
			java -jar scap-exec-1.2.5.jar -c scap_gov.nist_cref_r1800-ocil-xccdf1.xml -p xccdf_gov.nist.r1800-ocil_profile_cpe_applicability_1 r1800-ocil-datastream.xml -f results-r1800-ocil-datastream-3.xml
		step: 2.b
			java -jar scap-exec-1.2.5.jar -c scap_gov.nist_cref_r1800-ocil-xccdf1.xml r1800-ocil-datastream.xml -f results-r1800-ocil-datastream-4.xml
			
		step: 3.a
			java -jar scap-exec-1.2.5.jar -c scap_gov.nist_cref_r1800-ocil-xccdf1.xml -p xccdf_gov.nist.r1800-ocil_profile_cpe_applicability_1 r1800-ocil-datastream.xml -f results-r1800-ocil-datastream-5.xml
		step: 3.b
			java -jar scap-exec-1.2.5.jar -c scap_gov.nist_cref_r1800-ocil-xccdf2.xml -p xccdf_gov.nist.r1800-ocil_profile_cpe_applicability_2 r1800-ocil-datastream.xml -f results-r1800-ocil-datastream-6.xml

				
Cleanup Instructions 
	None
[QueryItem="Authors & Papers"]
PREFIX : <http://www.semanticweb.org/thiago.dasilva/ontologies/2022/8/7/untitled-ontology-69#>

select ?paper ?author {
	?exp a :Experiment;
	 	:hasInformationAuthorshipDado ?authorship;
		:Name ?paper.
	?authorship :Author_name ?author.
}
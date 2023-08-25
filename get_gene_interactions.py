import sys
import requests


class GeneInteractionFinder:

    def __init__(self):

        self.string_api_url = "https://version-11-5.string-db.org/api"

    def query_gene_list(self, genes):


        output_format = "tsv-no-header"
        method = "network"
        request_url = "/".join([self.string_api_url, output_format, method])

        params = {
            "identifiers" : "%0d".join(genes),
            "species" : 9606,                  # Human
            "add_nodes": len(genes) * 2        
        }
        
        response = requests.post(request_url, data=params)

        counted = set()
        unique_genes = []
        for g in genes:
            unique_genes.append([g, 0]) 

        for r in response.text.split("\n"):
            fields = r.rstrip().split("\t")
            if len(fields) > 1:
                g1, g2 = fields[2], fields[3]

                if not g1 in counted and g1 not in genes:
                     unique_genes.append([g1, 1])

                if not g2 in counted and g2 not in genes:
                     unique_genes.append([g2, 1])       

                counted.add(g1)
                counted.add(g2)

        return(unique_genes, response.text.split("\n"))
        

    def get_png(self, genes):


        output_format = "image"
        method = "network"
        request_url = "/".join([self.string_api_url, output_format, method])

        params = {
            "identifiers" : "%0d".join(genes),
            "species" : 9606,                  # Human
            "add_nodes": len(genes) * 2        
        }
        
        response = requests.post(request_url, data=params)
        return(response.content)


if __name__ == "__main__":

    query_genes = []
    pfx = sys.argv[2]
    with open(sys.argv[1]) as gwas_file:
        for gene in gwas_file:
            query_genes.append(gene.rstrip())

    geneIF = GeneInteractionFinder()
    netork_genes, full_edge_list = geneIF.query_gene_list(query_genes)
    with open(f'{pfx}.tsv', 'w') as tsv_out:
        for ng in netork_genes:
            print(f"{ng[0]}\t{ng[1]}", file=tsv_out)

    with open(f'{pfx}_edgelist.tsv', 'w') as edge_list_out:
        for e in full_edge_list:
            print(e.rstrip(), file=edge_list_out)

    """
    img_data = geneIF.get_png(query_genes)
    with open(f"{{pfx}.png", 'wb') as fh:
        fh.write(img_data)
    """
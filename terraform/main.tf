resource "kubernetes_namespace" "argocd" {
  metadata {
    name = "argocd"
  }
}

resource "kubernetes_namespace" "helloops" {
  metadata {
    name = "helloops"
  }
}
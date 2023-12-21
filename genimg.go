package main

import (
  "os"
  "time"
  "math/rand"
  "strings"
  "errors"
  "strconv"
  "fmt"
  "log"
  "image"
  "image/png"
  "image/color"
  "image/draw"
  "encoding/json"
  "io/ioutil"
)

var (
    totalnumber = os.Args[1];
    total,terr = strconv.Atoi(totalnumber);
    absaddress = os.Args[2];
    width = os.Args[3];
    wid,werr = strconv.Atoi(width)
    height = os.Args[4];
    hei,herr = strconv.Atoi(height);
    symbol = os.Args[5];
    name = os.Args[6];
    royalties = os.Args[7];
    royal,rerr = strconv.ParseInt(royalties,0,64);
    description = os.Args[8];
    exturl = os.Args[9];
    collectionname = os.Args[10];
    collectionfamily = os.Args[11];
    address = os.Args[12];
    numlayer = os.Args[13];
    layernum,lerr = strconv.Atoi(numlayer);
)

func trim_string(trait string) string {
  spstr := strings.Split(trait,"_")
  restr := ""
  if len(spstr) == 1 {
    restr = spstr[0]
  }
  if len(spstr) > 1 {
    for i, k := range spstr {
      restr+=k
      if i != len(spstr)-1 {
        restr+= " "
      }
    }
  }
  return restr
}

func getallsub(nl int) []string {
    var subs []string
    for k:=0;k<nl;k++ {
        var n string
        fmt.Println("if absaddress == ~/home/absc/Desktop/layers/; then layer input is folder name inside layers folder")
        fmt.Println("the layer from base to top: ")
        fmt.Scanln(&n)
        n=absaddress+n
        subs = append(subs,n)
    }
    return subs
}

var subs = getallsub(layernum)

func get_number(w string,b int) string {
  a := ""
  if b < 10 {
    a = fmt.Sprintf("%s #0000%d",w,b)
  }
  if b > 9 && b < 100 {
    a = fmt.Sprintf("%s #000%d",w,b)
  }
  if b > 99 && b < 1000 {
    a = fmt.Sprintf("%s #00%d",w,b)
  }
  if b > 999 && b < 10000 {
    a = fmt.Sprintf("%s #0%d",w,b)
  }
  if b > 9999 && b < 100000 {
    a = fmt.Sprintf("%s #%d",w,b)
  }
  return a
}

func faiLog(e error) {
  if e != nil {
    fmt.Println(e)
    log.Fatal("error!")
    panic(e)
  }
}

func genFromArray(arr []fileNames, len int) string {
  rand.Seed(time.Now().UnixNano())
  index := rand.Intn(len)
  return arr[index].name
}

type fileNames struct {name string}

func getFileNames(dir string) []fileNames {
  fileInfos, err := ioutil.ReadDir(dir)
  if err != nil {
    fmt.Println("Error in accessing directory:", err)
  }

  pngCounter := 0

  for _, k := range fileInfos {
    if strings.HasSuffix(k.Name(),".png") {
      pngCounter += 1
    }
  }

  fileInDir := make([]fileNames,0,pngCounter)

  for _, filename := range fileInfos {
    if strings.HasSuffix(filename.Name(),".png") {
      address:=strings.Join(strings.Split(filename.Name(),".png"),"")
      fileInDir = append(fileInDir,fileNames{address})
    }
  }

  return fileInDir
}

func isFolder(address string) {
  if _, err := os.Stat(address); errors.Is(err,os.ErrNotExist) {
    err := os.Mkdir(address,os.ModePerm)
    if err != nil {
      log.Println(err)
    }
  }
}

func fullAddressParentDir() string {
  path, err := os.Getwd()
  if err != nil {
    log.Println(err)
  }
  return path
}

func timeunix() int64 {
  now := time.Now().Unix()
  return now
}

type NFTTrait struct {
  Trait_type string `json:"trait_type"`
  Value string `json:"value"`
}

type NFTFile struct {
  Uri string `json:"uri"`
  Medium_type string `json:"type"`
}

type NFTCreator struct {
  Address string `json:"address"`
  Share int64 `json:"share"`
}

type NFTAuthor struct {
  Author_name string `json:"author_name"`
}

type NFTProperties struct {
  Files []NFTFile `json:"files"`
  Category string `json:"category"`
  Creators []NFTCreator `json:"creators"`
}

type NFTCollection struct {
  Name string `json:"name"`
  Family string `json:"family"`
}

type SolanaMetaplexNFTMetadata struct {
  Name string `json:"name"`
  Symbol string `json:"symbol"`
  Description string `json:"description"`
  Seller_fee_basis_points int64 `json:"seller_fee_basis_points"`
  ExternalURL string `json:"external_url"`
  Image string `json:"image"`
  Collection NFTCollection `json:"collection"`
  Properties NFTProperties `json:"properties"`
  Attributes []NFTTrait `json:"attributes"`
  Compiler string `json:"compiler"`
}

type ERC721NFTMetadata struct {
  Name string `json:"name"`
  Description string `json:"description"`
  Image string `json:"image"`
  Attributes []NFTTrait `json:"attributes"`
}

func main() {
  if layernum < 2 {
    fmt.Println("require more than 1 layer")
    panic(lerr)
  }
  var j [][]fileNames
  for i:=0;i<layernum;i++{
    f := getFileNames(subs[i])
    j = append(j,f);
  }

  comb_710 := make([]string,0,total)

  for len(comb_710) != total {
    comb := genFromArray(j[0],len(j[0]))+"-"
    
    for k:=1;k<len(j);k++ {
        comb+=genFromArray(j[k],len(j[k]))
        if k != len(j)-1 {
            comb+="-"
        }
    }

    binary := false

    for _, x := range comb_710 {
      if x == comb {
        binary = true
        break
      }
    }

    if binary == false {
      comb_710=append(comb_710,comb)
    }
  }

  isFolder("assets")

  for i, loop := range comb_710 {
    bgImg := image.NewRGBA(image.Rect(0, 0, wid, hei))
    draw.Draw(bgImg, bgImg.Bounds(), &image.Uniform{color.RGBA{0,0,0,0}}, image.ZP, draw.Src)

    offset := image.Pt(0,0)
    fmt.Println(loop)
    for w:=0;w<len(j);w++{
        split := strings.Split(subs[w], "/")
        open,err:=os.Open(absaddress+strings.TrimSpace(split[len(split)-2])+"/"+strings.Split(loop,"-")[w]+".png");
        faiLog(err)
        defer open.Close()
        img,_,err:=image.Decode(open)
        faiLog(err)
        draw.Draw(bgImg,img.Bounds().Add(offset),img,image.ZP,draw.Over)
        open.Close()
    }

    path := fmt.Sprintf("assets/%d.png",i)
    f,_ := os.Create(path)
    png.Encode(f,bgImg)

    f.Close()
    
    var ggla []NFTTrait
    
    for t:=0;t<len(subs);t++{
        split := strings.Split(subs[t], "/")
        hey := strings.TrimSpace(split[len(split)-2])
        ggla=append(ggla,NFTTrait{
          Trait_type: hey,
          Value: trim_string(strings.Split(loop,"-")[t]),
        })
    }

    solana_metaplex_meta := SolanaMetaplexNFTMetadata{
      Name: get_number(name,i+1),
      Symbol: symbol,
      Description: description,
      Seller_fee_basis_points: royal,
      ExternalURL: exturl,
      Image: fmt.Sprintf("%d.png",i),
      Collection: NFTCollection{
        Name: collectionname,
        Family: collectionfamily,
      },
      Properties: NFTProperties{
        Files: []NFTFile{
          NFTFile{
            Uri: fmt.Sprintf("%d.png",i),
            Medium_type: "image/png",
          },
        },
        Category: "image",
        Creators: []NFTCreator{
          NFTCreator{
            Address: address,
            Share:100,
          },
        },
      },
      Attributes: ggla,
      Compiler: "Maddy Generator",
    }

    erc721_meta := ERC721NFTMetadata{//not going to use
      Name: get_number("",i+1),
      Description: "",
      Image: fmt.Sprintf("%d.png",i),
      Attributes: []NFTTrait{
        NFTTrait{
          Trait_type: "background",
          Value: trim_string(strings.Split(loop,"-")[0]),
        },
      },
    }

    if i == -1 {fmt.Println(erc721_meta)} 

    content, err := json.Marshal(solana_metaplex_meta)

    faiLog(err)

    err = ioutil.WriteFile(fmt.Sprintf("assets/%d.json",i),content,0644)

    faiLog(err)
  }
}
